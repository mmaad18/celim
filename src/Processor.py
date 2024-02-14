from skimage import feature
import matplotlib.pyplot as plt


def detect_blobs(image, color='red', name='blobs'):
    blobs_log = feature.blob_log(
        image=image,
        min_sigma=10,
        max_sigma=30,
        num_sigma=1,
        threshold=.1,
        overlap=0.9,
    )

    fig, ax = plt.subplots(1, 1, figsize=(9, 8))
    ax.imshow(image, cmap='gray')

    for blob in blobs_log:
        y, x, r = blob
        c = plt.Circle((x, y), r, color=color, linewidth=1, fill=False)
        ax.add_patch(c)

    plt.axis('off')
    plt.savefig(f'out/{name}.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
    plt.close()

    return len(blobs_log)


