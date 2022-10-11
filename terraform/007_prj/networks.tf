data "aws_subnet" "selected" {
    id = var.var_subnet_id
}

resource "aws_security_group" "instance_jgz" {
  name        = "sec_grp_jgz"
  description = "this is a security group"
  vpc_id      = data.aws_subnet.selected.vpc_id

  ingress {
    description      = "apache http"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    #cidr_blocks      = [aws_vpc.main.cidr_block]
    #ipv6_cidr_blocks = [aws_vpc.main.ipv6_cidr_block]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    #ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "jeangiono_secgrp"
  }
}

resource "aws_security_group_rule" "ssh" {
  security_group_id = aws_security_group.instance_jgz.id
  description = "ssh for ansible"
  type = "ingress"
  from_port = 22
  to_port = 22
  protocol = "tcp"
  cidr_blocks = ["0.0.0.0/0"]
}