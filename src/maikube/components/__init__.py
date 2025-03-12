from pkg_resources import resource_filename
from kfp.components import load_component


def load_component(name):
    """Load kubeflow pipeline component from YAML file in this package."""
    return load_component(resource_filename('enta.api.pipelines.components', f'{name}.yaml'))