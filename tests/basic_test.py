import blurplefier

with open("images/input.png", "rb") as test_file:
    test_file_bytes = test_file.read()

extension, standard_output = blurplefier.convert_image(
    test_file_bytes, blurplefier.Methods.CLASSIC
)

with open(f"images/output_standard.{extension}", "wb") as output_file:
    output_file.write(standard_output)

extension, filtered_output = blurplefier.convert_image(
    test_file_bytes, blurplefier.Methods.FILTER
)

with open(f"images/output_filter.{extension}", "wb") as output_file:
    output_file.write(filtered_output)
