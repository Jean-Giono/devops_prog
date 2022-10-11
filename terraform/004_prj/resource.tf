resource "null_resource" "ahost" {
  for_each = var.hosts
  triggers = {
    my_val = each.value
  }
  provisioner "local-exec" {
    command = "echo '${each.key}' '${each.value}' >> myhosts.txt"
  }
}