I don't have enough time to build this now, I make it someday! Below is the knowledge I've gathered so far,

# How does a download manager work?
A download manager employs a method known as "multi-threading" to enhance the download process. In multi-threading, the download manager divides a file into smaller segments, often referred to as "**chunks**" Each of these chunks is then downloaded by a separate thread. To illustrate, consider a scenario where the file is 12 megabytes in size, and the download manager employs 4 threads. In this case, the first thread would download the initial 4 megabytes, the subsequent thread would retrieve the next 4 megabytes, and so forth. After all the chunks have been downloaded, the download manager assembles them into a single cohesive file, effectively completing the download. We'll talk more about it in technical terms later.

This approach optimizes the download process by utilizing multiple threads to download different parts of the file concurrently, resulting in improved speed and efficiency.


#### Table of content
1. [Determining filename & extension](#Determining-filename-&-extension)
2. [How a DM request a certain part fo a file](#How-a-DM-request-a-certain-part-fo-a-file)
3. [where are the chunks stored?](#where-are-the-chunks-stored?)


## Determining filename & extension

A download manager determines the file type (also known as the file extension) using a combination of methods that involve the HTTP response headers, the URL, and often the content of the downloaded file itself. Here's how it typically works:

1. **HTTP Headers:** When you request a file download from a web server, the server responds with an HTTP header that contains information about the file. One of the headers that helps identify the file type is the "Content-Type" header. This header provides the MIME type of the file, which indicates its nature and purpose. For example:

```http
HTTP/1.1 200 OK
Content-Type: application/zip
```

   In this case, the "Content-Type" header indicates that the downloaded file is a ZIP archive.

2. **URL Analysis:** The download manager can also infer the file type based on the URL from which the file is being downloaded. Many websites structure their URLs to include recognizable file extensions. For instance, a URL like `https://example.com/file.zip` suggests a ZIP file, while `https://example.com/image.png` implies a PNG image.

3. **File Signature (Magic Number):** Some file types have unique signatures, also known as "magic numbers," at the beginning of the file's binary data. Download managers can examine these initial bytes to identify the file type. For instance, the first few bytes of a PNG image file are `89 50 4E 47 0D 0A 1A 0A`, which is its magic number.



Download managers often use a combination of these methods to accurately determine the file type. This capability allows the manager to handle downloaded files appropriately, such as displaying the correct icon, associating the file with the right software, or organizing files into specific folders based on their types.

**Determining the File Name:**

The download manager usually derives the file name from the "Content-Disposition" header in the HTTP response. This header suggests a filename that the browser or download manager can use to save the file. For example:

```http
HTTP/1.1 200 OK
Content-Disposition: attachment; filename="example.zip"
```

In this case, the "Content-Disposition" header provides the suggested filename "example.zip." The download manager can use this information to save the downloaded file with the appropriate name.

Download managers often use a combination of these methods to accurately determine both the file type and the filename. This capability allows the manager to handle downloaded files appropriately, such as displaying the correct icon, associating the file with the right software, organizing files into specific folders, and saving files with meaningful names.




## How a DM request a certain part fo a file
A download manager (DM) can request a certain part of a file using a technique called "HTTP Range Requests." This method allows the DM to specify the byte range it wants to download from the server. This is particularly useful for resuming interrupted downloads or for downloading specific segments of a large file concurrently. Here's how it works:

1. **HTTP Range Requests:**

When a download manager wants to retrieve a specific part of a file, it sends an HTTP request to the server with a "Range" header indicating the desired byte range. The "Range" header is formatted as `bytes=start-end`, where `start` is the byte index where the requested range begins, and `end` is the byte index where the requested range ends.

For example, if the DM wants to download bytes 1000 to 1999 of a file, it sends an HTTP request with the "Range" header:

```http
GET /file.txt HTTP/1.1
Host: example.com
Range: bytes=1000-1999
```

The server processes this request and responds with a partial content, containing the requested byte range:

```http
HTTP/1.1 206 Partial Content
Content-Length: 1000
Content-Range: bytes 1000-1999/5000
Content-Type: text/plain

[Partial content here]
```

In this example, the server acknowledges the partial content request with a "206 Partial Content" status code and provides the content range in the "Content-Range" header. The download manager receives the partial content and appends it to the appropriate location in the downloaded file.

2. **Parallel Downloads and Ranges:**

Download managers often use HTTP Range Requests to achieve parallel downloading of different file segments. This is done by splitting the file into multiple chunks and requesting each chunk with a separate Range header. The download manager can then download these chunks concurrently, speeding up the download process.

For instance, if the DM is downloading a 10 MB file using four threads, each thread might request a different range, such as:

- Thread 1: Range bytes=0-2559
- Thread 2: Range bytes=2560-5119
- Thread 3: Range bytes=5120-7679
- Thread 4: Range bytes=7680-10240

By downloading different parts of the file in parallel, the download manager can take advantage of the available bandwidth and optimize the overall download speed.

HTTP Range Requests are a powerful technique that allows download managers to efficiently retrieve specific portions of files, manage partial content, and improve the user experience when dealing with large or interrupted downloads.



## where are the chunks stored?
Download managers store downloaded chunks in temporary files or in memory (RAM), depending on their design and configuration. The method used to put together the chunks and remake the file varies, but it generally involves merging the downloaded parts into a complete file. Here's how it typically works:

1. **Storage of Downloaded Chunks:**

Download managers typically allocate a temporary storage location to store the downloaded chunks. This could be on your computer's hard drive or in memory, depending on factors such as available storage space and the download manager's settings. Storing chunks in temporary files is a common approach, as it allows the download manager to efficiently manage and organize the downloaded data.

2. **Merging Chunks to Remake the File:**

Once all the chunks have been downloaded, the download manager begins the process of merging these chunks to create the complete file. The exact process can vary based on the download manager's internal mechanisms, but it generally follows these steps:

   a. **Ordering the Chunks:** The download manager ensures that the downloaded chunks are in the correct order. This is important to ensure that the data is merged correctly.

   b. **Appending Chunks:** The download manager starts by appending the data from each chunk to a new file or buffer, in the order of their download. This process continues until all chunks are merged.

   c. **Finalizing the File:** Once all chunks are merged, the download manager might perform additional tasks such as verifying the integrity of the merged data and checking for any missing or corrupted chunks.

   d. **Saving the Remade File:** Finally, the download manager saves the remade file to the designated download folder or the location specified by the user.

3. **Deleting Temporary Chunks:**

After the file is successfully remade, the download manager typically deletes the temporary downloaded chunks to free up storage space. This helps keep your storage clean and prevents unnecessary clutter.

By using this process, download managers are able to efficiently download large files in parallel chunks and then seamlessly merge these chunks to recreate the original file. This approach allows for faster downloads and provides mechanisms for resuming interrupted downloads or managing network errors during the download process.
