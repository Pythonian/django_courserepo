from django.shortcuts import get_object_or_404, render

from .models import Level, Library, Course, Material, ResourceType


def is_valid_query_paramter(param):
    return param != '' and param is not None


def home(request):
    levels = Level.objects.all()
    materials = Material.objects.order_by("?")[:8]
    courses = Course.objects.order_by("?")[:9]
    resource_types = ResourceType.objects.all()

    template_name = 'home.html'
    context = {
        'levels': levels,
        'materials': materials,
        'courses': courses,
        'resource_types': resource_types,
    }

    return render(request, template_name, context)


def courses(request):
    courses = Course.objects.all()

    template_name = 'courses.html'
    context = {
        'courses': courses,
    }

    return render(request, template_name, context)


def materials(request):
    materials = Material.objects.all()

    template_name = 'materials.html'
    context = {
        'materials': materials,
    }

    return render(request, template_name, context)


def course_material(request, slug):
    material = get_object_or_404(Material, slug=slug)

    template_name = 'course_material.html'
    context = {
        'material': material,
    }

    return render(request, template_name, context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    materials = Material.objects.filter(course=course)

    template_name = 'course_detail.html'
    context = {
        'course': course,
        'materials': materials,
    }

    return render(request, template_name, context)


def level(request, slug):
    level = get_object_or_404(Level, slug=slug)

    template_name = 'level.html'
    context = {
        'level': level,
    }

    return render(request, template_name, context)


def search(request):
    qs = Material.objects.all()
    levels = Level.objects.all()
    courses = Course.objects.all()
    resource_types = ResourceType.objects.all()

    material_name_query = request.GET.get('name')
    level_query = request.GET.get('level')
    resource_type_query = request.GET.get('resource_type')
    course_query = request.GET.get('course')

    if is_valid_query_paramter(material_name_query):
        qs = qs.filter(name__icontains=material_name_query)

    if is_valid_query_paramter(course_query):
        qs = qs.filter(course=course_query)

    if is_valid_query_paramter(level_query) and level_query != '-- Select Level --':
        qs = qs.filter(course__level=level_query)

    if is_valid_query_paramter(resource_type_query) and resource_type_query != '-- Select Resource Type --':
        qs = qs.filter(resource_type=resource_type_query)

    template_name = 'search.html'
    context = {
        'materials': qs, 'levels': levels,
        'courses': courses, 'resource_types': resource_types,
    }

    return render(request, template_name, context)
