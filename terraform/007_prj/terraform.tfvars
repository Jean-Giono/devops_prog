var_ami = "ami-0caef02b518350c8b"
var_instance_type = "t2.micro"

var_tag_name = "anEC2fromJGZ"
var_tag_author = "jeangiono"

var_user_data = <<-EOF
    #!/bin/bash
    sudo apt-get update
    sudo apt-get install -y apache2
    sudo systemctl start apache2
    sudo systemctl enable apache2
    sudo echo "<h1>Hello from Houston!</h1>" > /var/www/html/index.html
  EOF


var_subnet_id = "subnet-07f3737030dbcfded"