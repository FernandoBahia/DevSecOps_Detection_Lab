terraform {
  required_version = ">= 1.6.0"

  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

provider "local" {}

resource "local_file" "detection_lab_manifest" {
  filename = "${path.module}/detection-lab-manifest.txt"

  content = <<-EOT
    DevSecOps Detection Lab
    =======================

    Detection:
      Sigma: detections/sigma
      YARA: detections/yara

    Tests:
      Python: python/tests

    Container:
      Docker detection pipeline

    Orchestration:
      Kubernetes

    Environment:
      Detection Engineering Laboratory
  EOT
}
