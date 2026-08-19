output "lab_name" {
  description = "Detection lab name"
  value       = var.lab_name
}

output "environment" {
  description = "Detection lab environment"
  value       = var.environment
}

output "manifest_path" {
  description = "Generated detection lab manifest"
  value       = local_file.detection_lab_manifest.filename
}
