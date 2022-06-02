# Configure the AWS Provider
provider "aws" {
  region = var.region
}

# VPC Creation
resource "aws_vpc" "hitech_vpc" {
  cidr_block       = var.vpc_cidr

  tags = {
    Name = "hitech_vpc"
  }
}

#Subnet_01 Creation
resource "aws_subnet" "hitech_sub_01" {
  cidr_block       = var.sub01_cidr
  vpc_id           = aws_vpc.hitech_vpc.id
  
  tags = {
    Name = "hitech_sub_01"
  }
}

#Subnet_02 Creation
resource "aws_subnet" "hitech_sub_02" {
	cidr_block = var.sub02_cidr
	vpc_id = aws_vpc.hitech_vpc.id
	
	tags = {
    Name = "hitech_sub_02"
  }
}


# Internet gateway
resource "aws_internet_gateway" "Hitech_igw" {
  vpc_id = aws_vpc.hitech_vpc.id

  tags = {
    Name = "main"
  }
}


# Route Table creation
resource "aws_route_table" "example" {
  vpc_id = aws_vpc.hitech_vpc.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.Hitech_igw.id
  }
  
}













