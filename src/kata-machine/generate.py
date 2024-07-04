# import os
# import sys
#
# from mako.template import Template
# new_limit = 2000  # Example: Set a new limit of 2000
# sys.setrecursionlimit(new_limit)
#
#
# def find_next_folder(base_dir):
#     """Find the next available folder number."""
#     i = 1
#     while True:
#         folder_path = os.path.join(base_dir, f"day_{i}")
#         if not os.path.exists(folder_path):
#             return folder_path
#         i += 1
#
#
# def create_new_folder(base_dir):
#     """Create a new numbered folder."""
#     new_folder = find_next_folder(base_dir)
#     os.makedirs(new_folder)
#     return new_folder
#
#
# def generate_code(template_filename: str, output_filename: str, output_parent_folder: str, day_number: int,
#                   output_dir: str):
#     # Read Mako template file
#     with open(template_filename, 'r') as template_file:
#         template_content = template_file.read()
#
#     # initial_directory = f"{output_parent_folder}-{day_number}/{output_dir}"
#     # next_directory = f"{output_parent_folder}-{day_number + 1}/{output_dir}"
#
#     # Create output directory if it doesn't exist
#     # if os.path.exists(initial_directory):
#     #     os.makedirs(next_directory)
#     # else:
#     #     os.makedirs(initial_directory)
#
#     # Create Mako template object
#     template = Template(template_content)
#
#     # Generate code using Mako template
#     generated_code = template.render()
#
#     # Write exercises code to output file
#     output_file_path = os.path.join(output_dir, output_filename)
#     with open(output_file_path, 'w') as output_file:
#         output_file.write(generated_code)
#
#     print(f"Generated {output_filename} in {output_dir}")
#
#
# if __name__ == '__main__':
#
#     base_dir = 'kata-machine'
#     new_folder = create_new_folder(base_dir)
#
#     # generate_code(new_folder)
#
#     # Generate insertion sort implementation
#     generate_code('templates/insertion_sort.mako',
#                   'insertion_sort.py',
#                   'day',
#                   1,
#                   'exercises'
#                   )
#
#     # Generate insertion sort unit tests
#     generate_code('templates/test_insertion_sort.mako',
#                   'test_insertion_sort.py',
#                   'day',
#                   1,
#                   'tests'
#                   )
#
# TODO ------------------------------------------------------------------------ fix the code generation for the kata-machine

# import os
# from mako.template import Template
#
# # Function to create a new numbered folder
# def find_next_folder(base_dir):
#     i = 1
#     while True:
#         folder_path = os.path.join(base_dir, f"folder_{i}")
#         if not os.path.exists(folder_path):
#             return folder_path
#         i += 1
#
# # Function to create a new folder and generate code or tests inside it
# def create_new_folder_and_generate(base_dir, template_file):
#     # Find the next available folder
#     new_folder = find_next_folder(base_dir)
#     os.makedirs(new_folder)
#
#     # Generate content using the specified template
#     template = Template(filename=template_file)
#     rendered_content = template.render()
#
#     # Write rendered content to a file in the new folder
#     with open(os.path.join(new_folder, 'generated_content.txt'), 'w') as f:
#         f.write(rendered_content)
#
#     return new_folder
#
# def main():
#     base_dir = 'generated_folders'
#
#     # Generate code using code template
#     code_template_file = 'code_template.mako'
#     new_code_folder = create_new_folder_and_generate(base_dir, code_template_file)
#     print(f"Generated code in: {new_code_folder}")
#
#     # Generate tests using test template
#     test_template_file = 'test_template.mako'
#     new_test_folder = create_new_folder_and_generate(base_dir, test_template_file)
#     print(f"Generated tests in: {new_test_folder}")
#
# if __name__ == "__main__":
#     main()
