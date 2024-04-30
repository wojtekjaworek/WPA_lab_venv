import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re

# Check if packages are in the exact versions specified in requirements.txt
def check_packages_versions():
    required_packages = {'matplotlib': '3.4.2', 'numpy': '1.21.0', 'pandas': '1.3.0'}
    installed_versions = {}
    
    for package, required_version in required_packages.items():
        try:
            module = __import__(package)
            version = module.__version__
            installed_versions[package] = version
            match = re.match(r'^(\d+)\.(\d+)', version)
            if match:
                major_version, minor_version = map(int, match.groups())
                if major_version != int(required_version.split('.')[0]) or minor_version != int(required_version.split('.')[1]):
                    return False, installed_versions
            else:
                return False, installed_versions
        except ImportError:
            return False, installed_versions
    
    return True, installed_versions

# Check packages versions
compatible, installed_versions = check_packages_versions()

if not compatible:
    # Display the message on a plot
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, "Zainstalowane biblioteki są w innych wersjach niż w pliku requirements.txt",
            horizontalalignment='center', verticalalignment='center', fontsize=14)
    ax.axis('off')  # Turn off axes
    plt.show()
else:
    # Generate data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    # Create 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(x.flatten(), y.flatten(), z.flatten(), cmap='viridis')

    # Set labels and title
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('3D Plot of Function')

    # Show plot
    plt.show()
