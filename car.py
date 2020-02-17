class Car:
    def __init__(self, car_id, marca, modelo, anno, cilindrada, estilo, combustible, transmision, estado, kilometraje,
                 puertas, pagoImpuesto, negociable, recibeVehiculo, fechaIngreso, vecesVisto, comentarios, precio):
        self.car_id = car_id
        self.marca = marca
        self.modelo = modelo
        self.anno = anno
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
        self.precio = precio

    def get_csv(self):
        return '"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s"\n' % \
               (self.car_id, self.marca, self.modelo, self.anno, self.cilindrada, self.estilo, self.combustibile,
                self.transmision, self.estado, self.kilometraje, self.puertas, self.pagoImpuesto, self.negociable,
                self.recibeVehiculo, self.fechaIngreso, self.vecesVisto, self.comentarios, self.precio)