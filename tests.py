import blurplefier

test_file = open("test_images/input.png", "rb")
test_file_bytes = test_file.read()

extension, standard_output = blurplefier.convert_image(test_file_bytes, "blurplefy")

with open(f"test_images/output_standard.{extension}", "wb") as output_file:
    output_file.write(standard_output)

extension, filtered_output = blurplefier.convert_image(test_file_bytes, "filter")

with open(f"test_images/output_filter.{extension}", "wb") as output_file:
    output_file.write(filtered_output)
