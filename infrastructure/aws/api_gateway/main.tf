# API Gateway
resource "aws_apigatewayv2_api" "music_generator_apigateway" {
  name = var.api_gateway_name
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_stage" "music_generator_apigateway_stage" {
  api_id = aws_apigatewayv2_api.music_generator_apigateway.id
  name = var.stage_name
  auto_deploy = true
}

resource "aws_apigatewayv2_integration" "music_generator_apigateway_integration" {
  api_id = aws_apigatewayv2_api.music_generator_apigateway.id
  integration_type = "AWS_PROXY"
  integration_method = "POST"
  integration_uri = var.lambda_invoke_arn
  passthrough_behavior = "WHEN_NO_MATCH"
}

resource "aws_apigatewayv2_route" "music_generator_apigateway_route" {
  api_id = aws_apigatewayv2_api.music_generator_apigateway.id
  route_key = "ANY /{proxy+}"
  target = "integrations/${aws_apigatewayv2_integration.music_generator_apigateway_integration.id}"
}

resource "aws_lambda_permission" "api-gateway" {
  statement_id = "AllowExecutionFromAPIGateway"
  action = "lambda:InvokeFunction"
  function_name = var.lambda_arn
  principal = "apigateway.amazonaws.com"
  source_arn = "${aws_apigatewayv2_api.music_generator_apigateway.execution_arn}/*/*/*"
}

resource "aws_apigatewayv2_api_mapping" "music_generator_apigateway_integration" {
  api_id = aws_apigatewayv2_api.music_generator_apigateway.id
  domain_name = var.domain_name.id
  stage = aws_apigatewayv2_stage.music_generator_apigateway_stage.id
}

data "aws_route53_zone" "selected" {
  name = "music.andranjo.com."
  private_zone = false
}

resource "aws_route53_record" "record" {
  zone_id = data.aws_route53_zone.selected.zone_id
  name = var.api_gw_record_name
  type = "A"

  alias {
    name = var.domain_name.domain_name_configuration[0].target_domain_name
    zone_id = var.domain_name.domain_name_configuration[0].hosted_zone_id
    evaluate_target_health = false
  }
}

output "apigatewayv2_api_api_endpoint" {
  description = "Music Generator API endpoint"
  value = try(aws_apigatewayv2_api.music_generator_apigateway.api_endpoint, "")
}
