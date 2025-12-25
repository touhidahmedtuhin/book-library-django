from django.contrib import admin
from .models import Book , Author , Address

# Register your models here.
class BookAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ("author","rating",)
  list_display = ("title","author_name")

  def author_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"



admin.site.register(Book,BookAdmin)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name",)
    search_fields = ("first_name", "full_name",)

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street","postal_code","city",)





