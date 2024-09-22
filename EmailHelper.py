
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Your SendGrid API key
SENDGRID_API_KEY = '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'
TO_EMAIL = 'sonubhandari@microsoft.com'
FROM_EMAIL='sonuait135@gmail.com'

def send_email(subject, inputData):
    print("Email Start")
    body=''' <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
        }

        .container {
            /* max-width: 800px; */
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        table, th, td {
            border: 1px solid #ddd;
        }

        th, td {
            padding: 10px;
            text-align: left;
        }

        th {
            background-color: #007BFF;
            color: white;
        }

        #output {
            margin-top: 20px;
        }
    </style>
    <div id="output">
                <table id="dataTable">
                    <thead>
                        <tr>
                            <th>Comment Link</th>
                            <th>Comment Summary</th>
                            <th>Is Critical</th>
                            <th>Post Date</th>
                            <th>Post Link</th>
                            <th>Post Title</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- API data will be dynamically inserted here -->
                    '''

    user_dict = inputData.dict()

    try:
        if hasattr(inputData, 'json_dict') :
            json_dict = inputData.json_dict
            reddit = json_dict["reddit"]
            for data in reddit: 
                body = body + f'''<tr>
                                <td><a href="{data["comment_link"]}" target="_blank">Link</a></td>
                                <td>{data["comment_summary"]}</td>
                                <td>{data["critical"]}</td>
                                <td>{data["post_date"]}</td>
                                <td><a href="{data["post_link"]}" target="_blank">Post Link</a></td>
                                <td>{data["post_title"]}</td>
                            </tr>
                            </tr>'''
    except Exception as e:
        return print(str(e))

    body= body+''' </tbody>
                </table>
            </div>'''

    print(body)

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject=subject,
        html_content=body
    )
    
    try:
        print("email process start")
        #sg = SendGridAPIClient(SENDGRID_API_KEY)
        #response = sg.send(message)
        #print(f"Email sent! Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")


