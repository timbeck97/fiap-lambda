output "api_endpoint" {
  description = "URL do HTTP API Gateway"
  value       = aws_apigatewayv2_stage.default.invoke_url
}