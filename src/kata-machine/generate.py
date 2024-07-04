from mako.template import Template
import os

def generate_code(template_filename, output_filename, output_dir):
    # Read Mako template file
    with open(template_filename, 'r') as template_file:
        template_content = template_file.read()

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create Mako template object
    template = Template(template_content)

    # Generate code using Mako template
    generated_code = template.render()

    # Write exercises code to output file
    output_file_path = os.path.join(output_dir, output_filename)
    with open(output_file_path, 'w') as output_file:
        output_file.write(generated_code)

    print(f"Generated {output_filename} in {output_dir}")

if __name__ == '__main__':
    # Generate insertion sort implementation
    generate_code('templates/insertion_sort.mako', 'insertion_sort.py', 'exercises')

    # Generate insertion sort unit tests
    generate_code('templates/test_insertion_sort.mako', 'test_insertion_sort.py', 'tests')
