resource "aws_instance" "my_ec2" {
  #ami = "ami-06148e0e81e5187c8"
  # count = 2
  ami = "${data.aws_ami.test.id}"
  instance_type = "t2.micro"

  subnet_id = "subnet-07f3737030dbcfded"

  tags = {
    Name = "ec2_jgz"
    Author = "jeangiono"
  }
}