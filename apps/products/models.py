from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name=_('name'),
        help_text=_('Category name.')
    )
    main = models.ForeignKey(
        blank=True,
        null=True,
        to='self',
        on_delete=models.CASCADE,
        verbose_name=_('main category'),
        help_text=_('Main category'),
        related_name='sub_categories',
        related_query_name='main_category',
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')
        ordering = ('main', 'name',)


class Brand(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name=_('name'),
        help_text=_('Brand name.')
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = ('Brand')
        verbose_name_plural = ('Brands')
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name=_('name'),
        help_text=_('Product name.')
    )
    brand = models.ForeignKey(
        blank=False,
        null=True,
        to=Brand,
        on_delete=models.SET_NULL,
        verbose_name=_('brand'),
        help_text=_('Product brand.'),
        related_name='products',
        related_query_name='product',
    )
    category = models.ForeignKey(
        blank=False,
        null=True,
        to=Category,
        on_delete=models.SET_NULL,
        verbose_name=_('category'),
        help_text=_('Product category.'),
        related_name='products',
        related_query_name='product',
    )
    current_price = models.DecimalField(
        blank=False,
        null=False,
        max_digits=10,
        decimal_places=2,
        verbose_name=_('current price'),
        help_text=_('Product current price.')
    )
    raw_price = models.DecimalField(
        blank=False,
        null=False,
        max_digits=10,
        decimal_places=2,
        verbose_name=_('raw price'),
        help_text=_('Product raw price.')
    )
    likes_count = models.PositiveIntegerField(
        blank=True,
        null=False,
        default=0,
        verbose_name=_('likes count'),
        help_text=_('Product likes count.')
    )
    discount = models.PositiveIntegerField(
        blank=True,
        null=False,
        default=0,
        verbose_name=_('discount'),
        help_text=_('Product discount.')
    )
    is_new = models.BooleanField(
        blank=True,
        null=False,
        default=True,
        verbose_name=_('is new?'),
        help_text=_('Is the product new?'),
    )
    model = models.CharField(
        max_length=9,
        blank=False,
        null=False,
        verbose_name=_('model'),
        help_text=_('Product model.')
    )
    url = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('URL'),
        help_text=_('Product URL.')
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('image URL'),
        help_text=_('Product image URL.')
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = ('product')
        verbose_name_plural = ('products')
        ordering = ('category', 'brand')


class Variation(models.Model):
    product = models.ForeignKey(
        blank=False,
        null=False,
        to=Product,
        on_delete=models.CASCADE,
        verbose_name=_('product'),
        help_text=_('Product variation.'),
        related_name='variations',
        related_query_name='variation',
    )
    color = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name=_('color'),
        help_text=_('Variation color.')
    )
    thumbnail_url = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('thumbnail URL'),
        help_text=_('Variation thumbnail URL.')
    )
    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name=_('image URL'),
        help_text=_('Variation image URL.')
    )

    def __str__(self) -> str:
        return self.product

    class Meta:
        verbose_name = _('variation')
        verbose_name_plural = _('variations')
        ordering = ('product',)
