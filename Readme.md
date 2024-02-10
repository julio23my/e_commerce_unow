# Challenged test for a e-commerce functions

For this repository we going to complete the following goals

## Instalation

## First

    [ ] Clients can buy products.
    [ ] Know the total input.
    [ ] discount by country.
    [ ] promotional code on basket (only can apply one).
    [ ] products can have discounts

Diseño y implementación del back-end de un e-commerce

### *Aclaraciones*

    ● Por simplicidad, puedes trabajar sin unidad en los importes, sin divisa monetaria, guardando sólo el número. 15€ podrían ser 15.
    ● El lenguaje a usar es Python 3.x. El estilo, las buenas prácticas, la organización del diseño y la pulcritud del código no dependen del lenguaje de programación que se use ;)

### *¿Qué se evaluará?*

Tus conocimientos y habilidades de diseño y programación.

### *¿Qué debes hacer?*

El objetivo es conseguir estos incrementos de funcionalidad. Para ello no puedes usar persistencia (ej. base de datos, etc.) ni ningún framework (ej. Django, etc.). Aparte de estas restricciones, el diseño y la implementación del código es totalmente libre.
La idea es evaluar tus conocimientos puramente de Backend, es decir que desde consola puedas hacer algo tipo:

```python

prod = crea_producto()

añadir_al_carro(prod)

print(total_del_carro())

```

Puedes definir las clases, funciones, parámetros recibidos... que consideres oportuno. Hazlo lo mejor que sepas y ¡lúcete!

# 1. Primera parte

Formas parte del equipo de desarrollo de una plataforma ecommerce y en el sprint actual te has asignado la siguiente tarea:

**Back-end: Añadir productos con dto. en cesta y poder aplicar códigos promocionales en la cesta**

    ● El objetivo es que los clientes puedan comprar los productos. 

    ● Para esta versión simplificada, nos basta con saber el importe total de un carro con productos que el cliente ha añadido. 

    ● Por ejemplo, si el cliente añade un producto de 5€ y otro de 10€, el resultado esperado es que el programa devuelva que el total a pagar son 15€. 

    ● Los productos pueden tener un descuento (en función del país); y en la cesta, el cliente puede aplicar un código promocional. 

    ● A efectos prácticos, si un cliente compra un producto que tiene un dto del 10% y cuyo precio base es de 50€, el total a pagar sería de 45€. 
    
    ● Además, el cliente podría añadir un código promocional al carro que bajaría el precio total a pagar. 

*Requisitos:*

    Los productos pueden: 
        - Tener precios distintos según el país. Por ejemplo, 20€ en España pero 22€ en Italia. 

        - Tener un porcentaje de descuento sobre el precio (también en función del país). Por ejemplo 5% en España y ningún dato en Italia.

Los códigos promocionales se pueden añadir al carro. Estos códigos promocionales:

    ● Consisten en un descuento de importe fijo sobre el importe total de la cesta siempre que esté total supere un mínimo. Ejemplo: 10€ de dto. si la cesta supera 100€. 

    ● Un mismo código promocional es válido para todos los países. Es decir que son independientes del país.
    
    ● Un carro puede tener como máximo un solo código promocional.

**Caso 1**

Tenemos un **producto** A que se vende en España, Reino Unido e Italia.

    ● En España (código ES) se vende a 50€.

    ● En Reino Unido (código GB) el precio base es 55€ al que hay que aplicar un 10% de descuento 

    ● En Italia (código IT) el precio base es de 55€ al que hay que aplicar un 25% de descuento 

    Para un carro con 2 unidades del producto A: 
        ● En "ES" el precio total a pagar será de 100€. 
        ● En "GB" el precio total a pagar será de 99.0€ 
        ● En "IT" el precio total a pagar será de 82.5€.

**Caso 2**

    ● Tenemos un producto A que se vende en España con un precio base de 50€ al que hay que aplicar un 10% de descuento. 

    ● Tenemos un producto B que se vende en España a un precio final de 20€ (no tiene descuento). 

    ● Además tenemos un código promocional ("promo5") que aplica un descuento directo de 5€ si el cliente compra más de 90€. 

    ● Para un carro con 1 unidad del producto A y 1 unidad del producto B usando el código promocional "promo5", el precio total a pagar será de 65€ 

    ● Para un carro con 2 unidades del producto A y 1 unidad del producto B usando el código promocional "promo5", el precio total a pagar será de 105€

# 2. Segunda parte

Después de un tiempo con la tienda en marcha, como empresa hemos fijado el objetivo de aumentar el precio medio de las cestas. Es decir, que los clientes gasten más en cada compra.

Hemos analizado las cestas y hemos visto que la mayoría de compras incluyen solo una unidad de cada producto. Desde el departamento de marketing nos han recomendado implementar descuentos por cantidad para incentivar a los clientes a comprar más.

Nos han explicado que la mejor forma de aplicar los descuentos por cantidad es hacerlo por tramos. Por ejemplo, de 1 a 10 unidades no aplicamos descuento, de 11 a 20 unidades aplicamos un descuento, de 21 a 30 unidades aplicamos un descuento mayor, etc. También han comentado que como no todos los casos son iguales, nos interesará que unas veces el descuento sea de una cantidad fija, y otras veces que sea de un porcentaje sobre el precio del producto.

Los descuentos por cantidad son descuentos adicionales sobre el precio final del producto (es decir, el precio del producto con descuento si lo tiene). También hay que tener en cuenta que los descuentos de cada tramo no se acumulan y se aplican una sola vez.

Ejemplo: producto con precio 10€ con descuento de 2€ que nos da un precio de venta 8€. Descuentos por cantidad: más de 10 unidades aplicamos un 10% de descuento, significa que el precio de venta final si compramos más de 10 unidades será de 7,20€. Si compramos 20 o más unidades, el precio de venta final seguirá siendo de 7,20€ porque no hay ningún descuento definido para 20 o más unidades.

Desde el departamento técnico hemos decidido que implementaremos esta nueva funcionalidad en este sprint.

*Ejemplos de salida esperada*

Tenemos un **producto** A que se vende en España con un precio base de 50€ al que hay que aplicar un 10% de descuento.
Este producto A tiene además un descuento por cantidad fijo de 45€ para 3 o más unidades.
Tenemos un **producto** B que se vende en España a un precio final de 1.5€ (no tiene descuento).
Este producto B tiene además un descuento por cantidad configurado de la manera siguiente:

    ● Descuento fijo de 5€ a partir de 10 o más unidades.

    ● Descuento de tipo porcentaje del 10% a partir de 50 o más unidades. 

    ● Descuento de tipo porcentaje del 20% a partir de 200 o más unidades.

Adicionalmente tenemos un **código promocional** ("promo100") que aplica un descuento directo de 100€ si el cliente compra más de 200€.

    ● Para un carro con 1 unidad del producto A y 1 unidad del producto B usando el código promocional "promo100", el precio total a pagar será de 46.5€.

    ● Para un carro con 3 unidades del producto A y 9 unidades del producto B usando el código promocional "promo100", el precio total a pagar será de 103.5€.

    ● Para un carro con 3 unidades del producto A y 10 unidades del producto B usando el código promocional "promo100", el precio total a pagar será de 100€.

    ● Para un carro con 3 unidades del producto A y 60 unidades del producto B usando el código promocional "promo100", el precio total a pagar será de 171€.

    ● Para un carro con 4 unidades del producto A y 110 unidades del producto B usando el código promocional "promo100", el precio total a pagar será de 183.5€.

    ● Para un carro con 6 unidades del producto A y 200 unidades del producto B usando el código promocional "promo100", el precio total a pagar será de 365€.
