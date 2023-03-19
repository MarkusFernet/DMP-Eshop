from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Category Table implimented with MPTT.
    """

    name = models.CharField(
        verbose_name=("Category Name"),
        help_text=("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=("Category safe URL"), max_length=255, unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """
    ProductType Table will provide a list of the different types
    of products that are for sale.
    """

    name = models.CharField(verbose_name=("Product Name"), help_text=("Required"), max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Product Type")
        verbose_name_plural = ("Product Types")

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    """
    The Product Specification Table contains product
    specifiction or features for the product types.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=("Name"), help_text=("Required"), max_length=255)

    class Meta:
        verbose_name = ("Product Specification")
        verbose_name_plural = ("Product Specifications")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table contining all product items.
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(
        verbose_name=("title"),
        help_text=("Required"),
        max_length=255,
    )
    description = models.TextField(verbose_name=("description"), help_text=("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=("Regular price"),
        help_text=("Maximum 9999"),
        error_messages={
            "name": {
                "max_length": ("The price must be between 0 and 9999."),
            },
        },
        max_digits=4,
        decimal_places=0,
    )
    discount_price = models.DecimalField(
        verbose_name=("Discount price"),
        help_text=("Maximum 9999"),
        error_messages={
            "name": {
                "max_length": ("The price must be between 0 and 9999."),
            },
        },
        max_digits=4,
        decimal_places=0,
    )
    is_active = models.BooleanField(
        verbose_name=("Product visibility"),
        help_text=("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=("value"),
        help_text=("Product specification value (maximum of 255 words"),
        max_length=255,
    )

    class Meta:
        verbose_name = ("Product Specification Value")
        verbose_name_plural = ("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    """
    The Product Image table.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(
        verbose_name=("image"),
        help_text=("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=("Alternative text"),
        help_text=("Please add alternative text"),
        default="Responsive image",
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Product Image")
        verbose_name_plural = ("Product Images")
