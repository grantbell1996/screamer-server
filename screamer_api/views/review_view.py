"""View module for handling requests about game types"""
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from screamer_api.models.Director import Director
from screamer_api.models.Movie import Movie
from screamer_api.models.Genre import Genre
from screamer_api.models.Review import Review
from screamer_api.serializers import ReviewSerializer
from screamer_api.models import Actor

class ReviewView(ViewSet):
    """actors view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single actor type
        
        Returns:
            Response -- JSON serialized actor type
        """
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all actors"""


        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized actor instance
        """
        movie = Movie.objects.get(pk=request.data["movie"])
        
        review = Review.objects.create(
            user = request.auth.user,
            movie = movie,
            body = request.data["body"],
            rating = request.data["rating"],
            )

        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a review

        Returns:
            Response -- Empty body with 204 status code
        """

        review = Review.objects.get(pk=pk)
        review.user = request.auth.user
        review.body = request.data["body"]
        review.rating = request.data["rating"]
        
        
        movie = Movie.objects.get(pk=request.data["movie"])
        review.movie = movie
        
        review.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

