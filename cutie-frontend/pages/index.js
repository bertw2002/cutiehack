import Head from 'next/head';
import Link from 'next/Link';

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2 bg-purple-600 bg-opacity-25">
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="flex flex-col items-center justify-center w-full flex-1 px-20 text-center">
        <h1 className="text-6xl object-top font-mono">
          Scotty's Smart Mart

        </h1>
        <br />
        <div class="rounded w-3/5 text-lg h-96 bg-purple-400 bg-opacity-50 font-mono">

          Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?
        </div>
<br />
        <Link href="/main"><a>
          <button class="bg-purple-500 hover:bg-purple-400 text-white font-bold py-2 px-4 border-b-4 border-purple-700 hover:border-purple-500 rounded">
            See what our page does!
          </button>
        </a></Link>
      </main>


      <footer className="flex items-center justify-center w-full h-20 border-t bg-purple-100 bg-opacity-50">
        <a
          className="flex items-center justify-center font-mono"
          target="_blank"
          rel="noopener noreferrer"
        >
          Developed by albert wan, sebastian wueste, and damian ramos

        </a>
      </footer>
    </div>
  )
}
