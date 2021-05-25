from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .data_sources.github_spider import load_github_spider_results


class GithubViewSet(ViewSet):

    @action(detail=False, methods=["POST"])
    def load_github_spider_results(self, request):
        load_github_spider_results()
        return Response("Results have been loaded")
