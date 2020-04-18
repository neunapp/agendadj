from django.db import models
#
from django.db.models import Count


class ReunionManager(models.Manager):

    def cantidad_reuniones_job(self):
        resultado = self.values('persona__job').annotate(
            cantidad=Count('id')
        )
        print('**************')
        print(resultado)
        return resultado