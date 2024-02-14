class Producto:
    id=0
    nombre=""
    descripcion=""
    precio=0.0
    stock   =""

    def __init__(self, p_id, p_nombre, p_descripcion, p_precio, p_stock,p_imagen):
        self.id=p_id
        self.nombre=p_nombre
        self.descripcion=p_descripcion
        self.precio=p_precio
        self.stock=p_stock
        self.imagen=p_imagen
    def obtenerObjetoSerializable(self):
        dicctemp=dict()
        dicctemp["id"]=self.id
        dicctemp["nombre"]=self.nombre
        dicctemp["descripcion"]=self.descripcion
        dicctemp["precio"]=self.precio
        dicctemp["stock"]=self.stock
        dicctemp["imagen"]=self.imagen
        return dicctemp

    def __str__(self):
        return "User(id='%s')" % self.id