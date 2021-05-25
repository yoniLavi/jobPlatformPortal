from django.core.management import BaseCommand
from apps.portal.models import JobOffer


class Command(BaseCommand):

    def populate_job_offers(self, *args, **options):

        example_data = {
            "platform": "workable",
            "company": "axur",
            "raw_json": "{'id': 1575819, 'shortcode': '9230F5FC75', 'title': 'Front-End Engineer - Senior', 'remote': True, 'location': {'country': 'Brazil', 'countryCode': 'BR', 'city': 'São Paulo', 'region': 'State of São Paulo'}, 'state': 'published', 'isInternal': False, 'code': '', 'published': '2021-04-06T00:00:00.000Z', 'type': 'full', 'language': 'en', 'department': ['Engineering'], 'accountUid': '797115ef-cb08-461e-af28-8d86b1972d22', 'approvalStatus': 'approved', 'description': '<p>Axurians são profissionais apaixonados! Nós valorizamos a obsessão por eficiência e confiamos em pessoas maduras para lidar com toda a liberdade que proporcionamos no nosso ambiente! Entendemos que o respeito e o sentimento de dono são essenciais para manter o clima da nossa cultura e o relacionamento com o cliente sempre excelente. Nos guiamos por dados e a humildade intelectual deve sempre acompanhar nossos posicionamentos.</p><p><strong>Você curte inovação? Ama programar? Já pensou em trabalhar com desenvolvimento e ajudar a tornar a internet um local mais seguro? </strong>Buscamos um(a) desenvolvedor(a) front-end para trabalhar no nosso time de Engenharia, de forma remota ou presencial no escritório de Porto Alegre. Queremos uma pessoa para colaborar no desenvolvimento de um produto em fase de amplo crescimento e que vem dominando o mercado brasileiro de monitoramento de riscos digitais.</p><p>Um dia típico de trabalho pode incluir:</p><ul> <li>Todas as responsabilidades relacionadas diretamente a desenvolvimento de software, desde a definição colaborativa de requisitos até a manutenção - passando por design, implementação, testes automatizados e outras atividades.</li> <li>Planejar, desenvolver, testar e organizar o código front-end, incluindo HTML, CSS e JavaScript;</li> <li>Colaborar com UX designers e outros desenvolvedores para atingir o melhor resultado dentro do prazo esperado;</li> <li>Propor soluções inovadoras e que permitam a evolução constante do produto;</li> </ul>', 'requirements': '<p>Para um desenvolvedor são indispensáveis:</p><ul> <li>Ao menos três anos de experiência profissional relevante com desenvolvimento front-end;</li> <li>Domínio sólido de React, Node.js e testes automatizados nesses ambientes, além de boas práticas de programação;</li> <li>Noções de cloud computing e uso de IaaS.</li> <li>Saber lidar com liberdade e autonomia no ambiente de trabalho;</li> </ul><p>São considerados diferenciais importantes:</p><ul> <li>Graduação concluída em Ciência da Computação, Engenharia de Computação ou cursos similares;</li> <li>Inglês avançado;</li> <li>Experiência com continuous delivery, infrastructure as code, test-driven development e domain-driven design;</li> <li>Proficiência em tecnologias como Redux, Webpack, Jest, TypeScript, AWS, Docker e Git;</li> <li>Noções básicas de Java e Python.</li> </ul>', 'benefits': '<ul> <li>Vale refeição ou alimentação;</li> <li>Auxílio home office para montar seu escritório remoto (válido para quem optar pela modalidade 100% remoto);</li> <li>Planos de saúde e odontológico integrais (Bradesco Top Nacional);</li> <li>Horários flexíveis;</li> <li>Bônus de até um salário anual atrelado à resultados da empresa;</li> <li>Possibilidade de Stock Options.</li> </ul>'}",
            "url": "https://apply.workable.com/api/v2/accounts/axur/jobs/9230F5FC75",
            "application_url": "https://apply.workable.com/axur/j/9230F5FC75/apply/",
            "platform_id": "1575819",
            "title": "Front-End Engineer - Senior",
            "location": "Brazil",
            "department": "Engineering",
            "description": "<p>Axurians são profissionais apaixonados! Nós valorizamos a obsessão por eficiência e confiamos em pessoas maduras para lidar com toda a liberdade que proporcionamos no nosso ambiente! Entendemos que o respeito e o sentimento de dono são essenciais para manter o clima da nossa cultura e o relacionamento com o cliente sempre excelente. Nos guiamos por dados e a humildade intelectual deve sempre acompanhar nossos posicionamentos.</p><p><strong>Você curte inovação? Ama programar? Já pensou em trabalhar com desenvolvimento e ajudar a tornar a internet um local mais seguro? </strong>Buscamos um(a) desenvolvedor(a) front-end para trabalhar no nosso time de Engenharia, de forma remota ou presencial no escritório de Porto Alegre. Queremos uma pessoa para colaborar no desenvolvimento de um produto em fase de amplo crescimento e que vem dominando o mercado brasileiro de monitoramento de riscos digitais.</p><p>Um dia típico de trabalho pode incluir:</p><ul> <li>Todas as responsabilidades relacionadas diretamente a desenvolvimento de software, desde a definição colaborativa de requisitos até a manutenção - passando por design, implementação, testes automatizados e outras atividades.</li> <li>Planejar, desenvolver, testar e organizar o código front-end, incluindo HTML, CSS e JavaScript;</li> <li>Colaborar com UX designers e outros desenvolvedores para atingir o melhor resultado dentro do prazo esperado;</li> <li>Propor soluções inovadoras e que permitam a evolução constante do produto;</li> </ul>",
            "requirements": "<p>Para um desenvolvedor são indispensáveis:</p><ul> <li>Ao menos três anos de experiência profissional relevante com desenvolvimento front-end;</li> <li>Domínio sólido de React, Node.js e testes automatizados nesses ambientes, além de boas práticas de programação;</li> <li>Noções de cloud computing e uso de IaaS.</li> <li>Saber lidar com liberdade e autonomia no ambiente de trabalho;</li> </ul><p>São considerados diferenciais importantes:</p><ul> <li>Graduação concluída em Ciência da Computação, Engenharia de Computação ou cursos similares;</li> <li>Inglês avançado;</li> <li>Experiência com continuous delivery, infrastructure as code, test-driven development e domain-driven design;</li> <li>Proficiência em tecnologias como Redux, Webpack, Jest, TypeScript, AWS, Docker e Git;</li> <li>Noções básicas de Java e Python.</li> </ul>"
        }

        existing_job_offer = JobOffer.objects.all().count()

        if not existing_job_offer:
            job_offer = JobOffer(**example_data)
            job_offer.save()
            print("Job Offer added successfully to DB")
        else:
            print("DB already has existing JobOffers")

    def handle(self, *args, **options):
        self.populate_job_offers()


