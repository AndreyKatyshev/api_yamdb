from django.db import models


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
    )
    # title = models.ForeignKey(
    #     Title,
    #     on_delete=models.CASCADE,
    #     related_name='reviews',
    #     verbose_name='отзыв',
    # )
    text = models.TextField(
        'Текст отзыва',
        help_text='Напишите нам отзыв об этом произведении',
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )
    score = models.IntegerField(
        'оценка',  
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

    def __str__(self):
        return self.text[0:15]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    text = models.TextField(
        'Текст комментария',
        help_text='Как вам отзыв?',
    )
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        auto_now_add=True,
    )

    class Meta:
        ordering = ('created',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return f'комментарий: {self.text[0:15]}'


class Rating(models.Model):
    # author = models.ForeignKey(
    #     User,
    #     null=True,
    #     on_delete=models.CASCADE,
    #     related_name='score',
    #     verbose_name = 'оценьщик'
    # )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name = 'оцениваемое произведение'
    )
    rating = models.FloatField(
        related_name='ratings',
        verbose_name = 'оценка',
        null=True,
        blank=True,
    )
