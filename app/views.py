from django.http import JsonResponse
from twitter_client import client
from .models import Company, Comment
from .serializers import CompanySerializer, CommentSerializer
from rest_framework import generics


class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListByCompany(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Comment.objects.filter(company=company_id)


def fetch_tweets(request, company_id):
    company = Company.objects.get(id=company_id)

    # Get user ID of the company's Twitter account
    user = client.get_user(username=company.name)

    # Get recent tweets mentioning the user
    tweet_search_response = client.get_users_mentions(id=user.id, max_results=1, tweet_fields=[
                                                      'context_annotations', 'created_at'])

    if tweet_search_response.data:
        # Just get the first tweet
        tweet = tweet_search_response.data[0]
        # Create a new Comment for this tweet
        Comment.objects.create(
            company=company,
            text=tweet.text,
            # More fields here...
        )
        return JsonResponse({'message': 'Tweet fetched successfully', 'tweet': tweet.text})

    return JsonResponse({'message': 'No tweets found for this company'})
