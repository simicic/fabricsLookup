from marshmallow import Schema


class FabricSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'href')


fabric_schema = FabricSchema()
fabrics_schema = FabricSchema(many=True)
