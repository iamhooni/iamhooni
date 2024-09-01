from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Board

@csrf_exempt    
# 게시판 목록을 보여주는 뷰
def index(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'list.html', boards)

# 새로운 게시글을 작성하는 뷰
def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'post.html')

# 게시글 상세 페이지를 보여주는 뷰
def detail(request, id):
    board = get_object_or_404(Board, pk=id)  # 더 간결하고 오류 처리가 쉬운 get_object_or_404 사용
    return render(request, 'detail.html', {'board': board})

# 게시글을 수정하는 뷰
def Edit(request, id):
    board = get_object_or_404(Board, id=id)  # 수정할 게시글 가져오기
    if request.method == "POST":
        # POST 요청 시, 폼 데이터를 받아 게시글 객체를 업데이트합니다.
        board.author = request.POST.get('author', board.author)
        board.title = request.POST.get('title', board.title)
        board.content = request.POST.get('content', board.content)
        board.save()  # 변경된 내용을 저장합니다.
        return redirect('detail', id=board.id)  # 수정된 게시글 상세 페이지로 이동
    else:
        # GET 요청 시, 수정할 게시글의 기존 데이터를 폼에 채워서 보여줍니다.
        return render(request, 'edit.html', {'board': board})

# 게시글을 삭제하는 뷰
def Delete(request, id):
    # 요청이 POST인지 확인하여 삭제 작업을 진행
    if request.method == "POST":
        board = get_object_or_404(Board, id=id)  # 게시글 객체 가져오기
        board.delete()  # 게시글 삭제
        return redirect('index')  # 삭제 후 메인 페이지로 리디렉션
    else:
        return Http404("잘못된 요청입니다.")
