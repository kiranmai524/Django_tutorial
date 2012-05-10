# Create your views here.
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from polls.models import Choice, poll
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('polls/index.html')
    c = Context({
        'latest_poll_list': latest_poll_list,

        })
    return render_to_response('polls/index.html',{'latest_poll_list': latest_poll_list})
    return HttpResponse(t.render(c))
    output =' ,'.join([p.question for p in latest_poll_list])
    return HttpResponse(output)
    return HttpResponse("Hello,  World.. You\'re at the poll Index.")

def detail(request, poll_id):
    p=get_object_or_404(poll, pk=poll_id)
    try:
        p =  Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('polls/detail.html', {'poll' : p}),
                            context_instance=RequestContext(request))


    return HttpResponse("You\'re looking at poll %s." %poll_id)

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})
    return HttpResponse("You\'re looking at the results of poll %s." %poll_id)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))   
    return HttpResponse("You\'re voting on poll %s." % poll_id)
