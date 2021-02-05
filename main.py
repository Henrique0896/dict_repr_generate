from edit import Edit
from manipularArquivo import lerArquivo

arquivo = lerArquivo("models.py")


var = Edit(arquivo)
var.generate_dict_repr()