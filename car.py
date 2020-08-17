class Car:
    def __init__(self, car_id, marca, modelo, anno, anno_categoria, cilindrada, estilo, combustible, transmision, estado, kilometraje,
                 puertas, pagoImpuesto, negociable, recibeVehiculo, fechaIngreso, vecesVisto, comentarios, tiene_imagen, precio):
        self.car_id = car_id
        self.marca = marca
        self.modelo = modelo
        self.anno = anno
        self.anno_categoria = anno_categoria
        self.cilindrada = cilindrada
        self.estilo = estilo
        self.combustibile = combustible
        self.transmision = transmision
        self.estado = estado
        self.kilometraje = kilometraje
        self.puertas = puertas
        self.pagoImpuesto = pagoImpuesto
        self.negociable = negociable
        self.recibeVehiculo = recibeVehiculo
        self.fechaIngreso = fechaIngreso
        self.vecesVisto = vecesVisto
        self.comentarios = comentarios
        self.tiene_imagen = tiene_imagen
        self.precio = precio

    def get_csv(self):
        return '"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s"\n' % \
               (self.car_id, self.marca, self.modelo, self.anno, self.anno_categoria, self.cilindrada, self.estilo, self.combustibile,
                self.transmision, self.estado, self.kilometraje, self.puertas, self.pagoImpuesto, self.negociable,
                self.recibeVehiculo, self.fechaIngreso, self.vecesVisto, self.comentarios, self.tiene_imagen, self.precio)