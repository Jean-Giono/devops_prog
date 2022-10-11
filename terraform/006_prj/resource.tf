resource "null_resource" "ssh_target" {
  connection {
    type = "ssh"
    user = var.ssh_user
    host = var.hosts
    private_key = file(var.ssh_key)
  }

  provisioner "remote-exec" {
    inline = [
        "sudo apt update -qq >/dev/null",
        "sudo apt install -qq -y nginx >/dev/null"
    ]
  }

  provisioner "file" {
    source = "nginx.conf"
    destination = "/tmp/default"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo cp -a /tmp/default /etc/nginx/sites-available/default",
      "sudo systemctl restart nginx"
    ]
  }

  provisioner "local-exec" {
    command = "curl ${var.hosts}:6666"
  }

}