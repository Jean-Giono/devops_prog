resource "null_resource" "node1" {
  provisioner "local-exec" {
    command = "echo '${var.str}' > mystring.txt"
  }
}