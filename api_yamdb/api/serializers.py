from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


from review.models import Comment, Score, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Review
        read_only_fields = ('title',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('review',)


# class RatingSerializer(serializers.ModelSerializer):
#     rating = serializers.SerializerMethodField()

#     class Meta:
#         fields = '__all__'
#         model = Score
#         read_only_fields = ('title',)

#     def get_rating(self, obj):
