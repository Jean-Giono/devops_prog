variable "var_ami" {
  type = string
  description = "image server ami aws"
}

variable "var_instance_type" {
  type = string
  description = "type instance"
}

variable "var_tag_name" {
  type = string
  description = "La balise name de l'instance"
}

variable "var_tag_author" {
  type = string
  description = "La balise author de l'instance"
}

variable "var_user_data" {
  type = string
  description = "install apache2"
}

variable "var_subnet_id" {
  type = string
  description = "subnet_id en sous du VPC"
}

#variable "var_vpc_id" {
#  type = string
#  description = "id du VPC contenant notre instance"
#}

#variable "var_vpc_securitygroup_id" {
#  type = string
#  description = "id du groupe de sécurité lié au VPC contenant notre instance"
#}