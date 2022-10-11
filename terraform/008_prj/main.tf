data "aws_ami" "test" {
    #executable_users = ["self"]
    most_recent = true
    #name_regex = "^Ubuntu-\\d{3}"
    #owners = true

    filter{
        name = "name"
        #values = ["Ubuntu-*"]
        values = ["Ubuntu Server*"]
    }

    filter {
      name = "architecture"
      values = ["x86_64"]
    }

}

output "str" {
  value = data.aws_ami.test.id
}

output "str_name" {
  value = data.aws_ami.test.name
}