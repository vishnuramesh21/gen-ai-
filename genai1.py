from openai import OpenAI
client = OpenAI(
    api_key ='sk-proj-Hsr59GIba8PHD_rH8V-VerR42)B@ddqGijyD9gvq5hpEhE6u3040bqeeC_Ay807pk30v0fQRpT3816kFJLF6101j×LU/Keb6yysDs4x0L5NRd4eU3Ef7h5-j60f1sBUT1NhDo1TSXqdCI9MAuS0ULD4-WA'
)

response = client.responses.create(
    model='gpt-5.4-mini',
    input='thalapathi Vijay'
    

)
print(response.output_text)