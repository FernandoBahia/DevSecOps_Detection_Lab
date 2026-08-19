variable "lab_name" {
  description = "Name of the detection laboratory"
  type        = string
  default     = "devsecops-detection-lab"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "lab"
}
