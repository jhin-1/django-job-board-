from ...models import Job

class JobsOop:
    @staticmethod
    def all(request):
        re_data = None
        re_message = ""
        list_items = []
        get_all_items = Job.objects.all()
        for job in get_all_items:
            send = {
                "id": job.id,
                "title": job.title,
            }
            list_items.append(send)
        re_message = "pes"
        re_data = {
            "list_items": list_items,
        }
        return [re_message, re_data]