from skimage import feature
import matplotlib.pyplot as plt
import numpy as np


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


def saveHistogram(image, file_name):
    bins = np.arange(0, 1.001, 0.001)
    hist, bin_edges = np.histogram(image, bins=bins)

    plt.figure(figsize=(10, 3))
    plt.bar(bins[:-1], hist, width=0.001, color='black', edgecolor='black')
    plt.title('Pixel Intensity Distribution')
    plt.xlabel('Intensity Value')
    plt.ylabel('Pixel Count')
    plt.xlim([0, 1])
    plt.grid(axis='y', alpha=0.25)

    # Save the plot to a file
    plt.savefig(f'out/{file_name}_histogram.png', dpi=300, bbox_inches='tight', pad_inches=0.0)
    plt.close()

