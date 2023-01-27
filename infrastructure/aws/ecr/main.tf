resource "aws_ecr_repository" "ecr_private_repo" {
  name = var.ecr_repo_name
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
}

resource "aws_ecr_lifecycle_policy" "ecr_backend_retain_5_images" {
  repository = aws_ecr_repository.ecr_private_repo.name
  
  policy = jsonencode(
    {
      "rules": [
        {
          "rulePriority": 1,
          "description": "Keep last 5 images",
          "selection": {
            "tagStatus": "any",
            "countType": "imageCountMoreThan",
            "countNumber": 5
          },
          "action": {
            "type": "expire"
          }
        }
      ]
    }
  )
}


output "ecr_repo_url" {
  value = aws_ecr_repository.ecr_private_repo.repository_url
}
