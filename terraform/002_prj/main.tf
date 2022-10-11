
variable "str" {
  type=string
  default="this is a new string"
}

resource "null_resource" "node1" {
  provisioner "local-exec" {
    command = "echo '${var.str}' > string.txt"
  }
}

output "var_str" {
    value=var.str
}