resource "local_file" "file" {
    count = 3
    directory_permission = "0700"
    file_permission = "0700"
    #filename = "afile.txt"
    #content = "${ }${ }${ }${format("%03d", count.index+1)}${var.env}"
    filename = "filename${count.index}.txt"
    content = "${format("%03d", count.index+1)}${var.env}"
    
}