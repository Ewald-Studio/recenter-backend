import sys, inspect

def generate_serializers(app_name):
    module_name = f"{app_name}.models"
    module = sys.modules[module_name]
    models_names_list = []
    serializer_template = """class [NAME]Serializer(serializers.ModelSerializer):
    class Meta:
        model = [NAME]
        fields = '__all__'"""

    for name, obj in inspect.getmembers(module, lambda member: inspect.isclass(member) and member.__module__ == module_name):
        models_names_list.append(name)

    models_names = ", ".join(models_names_list)

    output  = "from rest_framework import serializers\n"
    output += f"from {module_name} import ({models_names})\n\n\n"
    output += "\n\n\n".join([serializer_template.replace('[NAME]', x) for x in models_names_list])

    return output


def generate_viewsets(app_name):
    module_name = f"{app_name}.models"
    module = sys.modules[module_name]
    models_names_list = []
    viewset_template = """class [NAME]ViewSet(viewsets.ModelViewSet):
    serializer_class = [NAME]Serializer
    queryset = [NAME].objects.all()"""

    for name, obj in inspect.getmembers(module, lambda member: inspect.isclass(member) and member.__module__ == module_name):
        models_names_list.append(name)

    models_names = ", ".join(models_names_list)
    serializers_names = ", \n".join([f"    {x}Serializer" for x in models_names_list])

    output  = "from rest_framework import viewsets, mixins\n"
    output += f"from {module_name} import ({models_names})\n\n\n"
    output += f"from .serializers import (\n{serializers_names}\n)\n\n\n"
    output += "\n\n\n".join([viewset_template.replace('[NAME]', x) for x in models_names_list])

    return output


def generate_urls(app_name):
    module_name = f"{app_name}.models"
    module = sys.modules[module_name]
    models_names_list = []

    for name, obj in inspect.getmembers(module, lambda member: inspect.isclass(member) and member.__module__ == module_name):
        models_names_list.append(name)

    output  = "from django.urls import path\n"
    output += "from django.conf.urls import url, include\n"
    output += "from rest_framework import routers\n"
    output += "from .viewsets import *\n"
    output += "\n"
    output += "router = routers.DefaultRouter()\n"
    output += "\n".join([f"router.register('{x.lower()}s', {x}ViewSet, basename='{x.lower()}s')" for x in models_names_list])
    output += "\n\n"
    output += "urlpatterns = [\n"
    output += "    url(r'^', include(router.urls)),\n"
    output += "]"

    return output


def generate_api(app_name, write_to_file=True):
    serializers = generate_serializers(app_name)
    print('==== SERIALIZERS ====')
    print(serializers)
    print('\n\n')

    viewsets = generate_viewsets(app_name)
    print('==== VIEWSETS ====')
    print(viewsets)
    print('\n\n')

    urls = generate_urls(app_name)
    print('==== URLS ====')
    print(urls)
    print('\n\n')

    if (write_to_file):
        f = open(f'{app_name}.api.py', 'w')
        f.write('# ==== SERIALIZERS ====\n')
        f.write(serializers)
        f.write('\n\n')
        f.write('# ==== VIEWSETS ====\n')
        f.write(viewsets)
        f.write('\n\n')
        f.write('# ==== URLS ====\n')
        f.write(urls)
        f.close()
