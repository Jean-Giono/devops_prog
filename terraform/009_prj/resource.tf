resource "aws_instance" "an_ec2" {
  #ami = "ami-06148e0e81e5187c8"
  count = 2
  #ami = var.var_ami
  #ami = lookup(var.var_ami)
  ami = element(var.var_ami, count.index)
  instance_type = var.var_instance_type

  vpc_security_group_ids = [aws_security_group.instance_jgz.id]

  key_name = aws_key_pair.deployer-ssh-key.key_name

  subnet_id = var.var_subnet_id
  
  user_data = var.var_user_data

  associate_public_ip_address = true

  tags = {
    #Name = var.var_tag_name
    #Name = "${count.index + 1}_${var.var_tag_name}"
    Name = element(var.var_tag_name, count.index)
    Author = var.var_tag_author
  }

}

resource "aws_key_pair" "deployer-ssh-key" {
  key_name = "deployer-key-jgz"
  public_key = file("~/.ssh/id_rsa.pub")
}