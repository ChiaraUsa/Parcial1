import unittest
from extract_data import extract_data  # Import your function here


class TestLambdaHandlerProcessing(unittest.TestCase):
    
    def test_lambda_handler_processing(self):
        # HTML de prueba
        html_content = """
            <div class="info-wrapper">
                <div class="listing-card__information-main">
                    <div class="listing-card__title-wrapper">
                        <div class="listing-card__title" content="¡tu Espacio Perfecto En Venta!  Apartamento En Venta En La Florida, Engativa. Bogotá.">
                            ¡tu Espacio Perfecto En Venta!  Apartamento En Venta En La Florida, Engativa. Bogotá.
                        </div>
                    </div>
                    <div class="listing-card__price-wrapper">
                        <div class="price">$ 158.000.000</div>
                    </div>
                    <div class="listing-card__location">Bogotá, D.C., Bogotá, D.C.</div>
                    <div class="listing-card__properties">
                        <div class="listing-card__property">
                            <div class="card-icon card-icon__bedrooms"></div>
                            <span content="3" data-test="bedrooms">3 habitaciones</span>
                        </div>
                    </div>
                    <div class="listing-card__facilities listing-card__facilities--separated">
                        <div class="facility-item">
                            <span class="facility-item__text">Gas natural</span>
                        </div>
                        <div class="facility-item">
                            <span class="facility-item__text">Agua</span>
                        </div>
                    </div>
                </div>
            </div>
        """

        # Llama a la función para extraer los datos
        extracted_data = extract_data(html_content)

        # Comprueba si los datos extraídos son correctos
        self.assertEqual(extracted_data, [['$ 158.000.000', 'No disponible', '3 habitaciones', 'Gas natural']])



if __name__ == '__main__':
    unittest.main()
