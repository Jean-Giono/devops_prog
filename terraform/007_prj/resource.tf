resource "aws_instance" "an_ec2" {
  #ami = "ami-06148e0e81e5187c8"
  #count = 1
  ami = var.var_ami
  instance_type = var.var_instance_type

  vpc_security_group_ids = [aws_security_group.instance_jgz.id]

  key_name = aws_key_pair.deployer-ssh-key.key_name

  subnet_id = var.var_subnet_id
  
  user_data = var.var_user_data

  associate_public_ip_address = true
  
  #filename = "filename${count.index}.txt"
  #${count.index+1}
  tags = {
    Name = var.var_tag_name
    #Name = "${count.index + 1}_${var.var_tag_name}"
    Author = var.var_tag_author
  }

}

resource "aws_key_pair" "deployer-ssh-key" {
  key_name = "deployer-key-jgz"
  public_key = file("~/.ssh/id_rsa.pub")
}