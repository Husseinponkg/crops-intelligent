class RegionConverter:
    regex = '[a-zA-Z ]+'  # Allow spaces in the region name

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)